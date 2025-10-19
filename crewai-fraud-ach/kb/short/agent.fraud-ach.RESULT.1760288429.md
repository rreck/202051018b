```json
{
  "id": "fcbf18bc2beb6a9a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288429,
  "host_pid": "9e6742732c60:1",
  "hash": "16e01158565a5bee34361e101e34543605f6d1f07e5acc72d4082fa8131f669d",
  "cid": "QmV116e01158565a5bee34361e101e34543605f6d1f0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288429,
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
      "evaluated_at": 1760288429
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
  "sig": "4ec0801af42ea46bfcd9b49c768f48783afa0bd2cc9522dbf49f0db677984ee0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029354583
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 93, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 92, 'first_seen': 1760285763, 'matching_hash': 'dbced9ae96be05e0'}}}een': 1760285764, 'matching_hash': '0d7de9a99f2e5847'}}}