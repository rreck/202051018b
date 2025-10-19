```json
{
  "id": "00bc87abead2e3d5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288701,
  "host_pid": "9e6742732c60:1",
  "hash": "ad33293506530f0f2b72b1a5165d10db855465610de8cf3b7ecf6f0e824421c4",
  "cid": "QmV1ad33293506530f0f2b72b1a5165d10db85546561",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288701,
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
      "evaluated_at": 1760288701
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
  "sig": "accba82733ce5bb9edf6cdc5bfeb4ebbf8de2b798908fa7b5f436831da9c1bf5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000247499118
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 101, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 100, 'first_seen': 1760285765, 'matching_hash': 'f65a723d753f6ade'}}}