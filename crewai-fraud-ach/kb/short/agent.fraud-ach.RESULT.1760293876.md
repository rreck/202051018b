```json
{
  "id": "deb32dec81a58435",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293876,
  "host_pid": "9e6742732c60:1",
  "hash": "8348a155f1096203e563560bf96ccf2359e6e68b4d59ff0890a8815252b4e412",
  "cid": "QmV18348a155f1096203e563560bf96ccf2359e6e68b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293876,
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
      "evaluated_at": 1760293876
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
  "sig": "75828df0807ae0b5ee7039db0e616894ce6f3f709234bd5cdb30e15a64f77202"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279768309
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 303, 'threshold': 50, 'total_amount': 25259595, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 302, 'first_seen': 1760284979, 'matching_hash': '8798983dc5a8227d'}}}