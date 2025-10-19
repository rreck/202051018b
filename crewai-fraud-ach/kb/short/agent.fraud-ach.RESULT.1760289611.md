```json
{
  "id": "832dabde55864e8c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289611,
  "host_pid": "9e6742732c60:1",
  "hash": "2378e47fc771b7ada7f62e9b92ca70c016a2b236770ee78ffe40034c3200a981",
  "cid": "QmV12378e47fc771b7ada7f62e9b92ca70c016a2b236",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289611,
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
      "evaluated_at": 1760289611
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
  "sig": "389cc9145d477900c85d3c097cc3f998b44cacbecd72b1ac79917e12478dc105"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027976584
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 128, 'threshold': 50, 'total_amount': 39498624, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 127, 'first_seen': 1760285763, 'matching_hash': '76d4e63915320a3d'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '053611749', 'validation_error': 'Invalid routing number checksum'}}}