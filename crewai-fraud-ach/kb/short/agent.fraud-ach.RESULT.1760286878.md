```json
{
  "id": "a8f845ad57cfe16d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286878,
  "host_pid": "9e6742732c60:1",
  "hash": "abe4312c205162d52f83294189d3b9e3643c03c14060623692908e1d05e2f904",
  "cid": "QmV1abe4312c205162d52f83294189d3b9e3643c03c1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286878,
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
      "evaluated_at": 1760286878
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
  "sig": "34b374db7e78683d51831a23b3d58400b39a41a8325a2457c18f2c36d2f25545"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000023386962
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 39, 'first_seen': 1760285765, 'matching_hash': '663df3e5258a7a87'}}}