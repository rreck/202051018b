```json
{
  "id": "324a52d986e964cc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289437,
  "host_pid": "9e6742732c60:1",
  "hash": "5f49e251aa72b396a098229418073dc7ba79886448a0a9072544865d7da77f3b",
  "cid": "QmV15f49e251aa72b396a098229418073dc7ba798864",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289437,
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
      "evaluated_at": 1760289437
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
  "sig": "4778628a82b949aeb261e93b7fb1590bda16c70f23e08c5112fdba8d0f1685f0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244838202
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 199, 'threshold': 50, 'total_amount': 47777910, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 198, 'first_seen': 1760284979, 'matching_hash': 'f90729670e1d4f48'}}}