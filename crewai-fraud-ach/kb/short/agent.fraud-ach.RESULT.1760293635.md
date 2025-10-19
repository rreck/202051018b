```json
{
  "id": "b7d4556ae4fa8730",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293635,
  "host_pid": "9e6742732c60:1",
  "hash": "b8363d969daa5809d6d373302449c4b54e3f44ec7a8c864c1a8f8b903711cd8e",
  "cid": "QmV1b8363d969daa5809d6d373302449c4b54e3f44ec",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293635,
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
      "evaluated_at": 1760293635
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
  "sig": "dabf0172bf90805cceb46ff01f73d19e7876c0dfbb372f2734d972ad25b4915d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029832912
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 222, 'threshold': 50, 'total_amount': 101851158, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 221, 'first_seen': 1760285765, 'matching_hash': 'ede6214022caf300'}}}