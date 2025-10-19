```json
{
  "id": "a834b2aa79253e05",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290039,
  "host_pid": "9e6742732c60:1",
  "hash": "7551fca45202f23ebbb5b0c93ef6d0c2183f8bd5ac515f912586aaa5543ccc4c",
  "cid": "QmV17551fca45202f23ebbb5b0c93ef6d0c2183f8bd5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290039,
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
      "evaluated_at": 1760290039
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
  "sig": "2996819ff7db95dce283b6b1a28ba3fad1c5da618fe55824bc4be7425db2cc63"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000033242654
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 140, 'threshold': 50, 'total_amount': 44625000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 139, 'first_seen': 1760285763, 'matching_hash': '1355ad48790eb31b'}}}