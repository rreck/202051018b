```json
{
  "id": "db0c9e066a528c7c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290383,
  "host_pid": "9e6742732c60:1",
  "hash": "843789873383f73239efccc652f1cd9054d47b020066845a88eb7880cdd2fe6e",
  "cid": "QmV1843789873383f73239efccc652f1cd9054d47b02",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290383,
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
      "evaluated_at": 1760290383
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
  "sig": "96df4b9381c8c3040e269fdf121365abcfdc29a9ca84a870ddf375ebfb04f2e3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029709484
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 149, 'threshold': 50, 'total_amount': 60989872, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 148, 'first_seen': 1760285763, 'matching_hash': 'f2d4d1f000649e92'}}}