```json
{
  "id": "cec0aefef0b52944",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288497,
  "host_pid": "9e6742732c60:1",
  "hash": "269d5da8143868dfe9eb06dabed6871ce122e31b0e9328a350ed238f680d994e",
  "cid": "QmV1269d5da8143868dfe9eb06dabed6871ce122e31b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288497,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760288497
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "5b1ba2d44c38c23cf2f0feb68811dc93ebf2f804f8e89f654a9b625d9cbc9291"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021222877
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 95, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 94, 'first_seen': 1760285765, 'matching_hash': 'c44c29fab5dec0d9'}}}een': 1760285763, 'matching_hash': 'c0f06a9b06ae007f'}}}