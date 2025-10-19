```json
{
  "id": "54ffcbce5fc185b1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289900,
  "host_pid": "9e6742732c60:1",
  "hash": "df36c2115446142c6eff01893c974b92c04c1f33190b44f153f0827afc07afcf",
  "cid": "QmV1df36c2115446142c6eff01893c974b92c04c1f33",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289900,
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
      "evaluated_at": 1760289900
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
  "sig": "1481c606dd28ba4795e571320e1ea8be251b73ad2a3f172e1a725a2a37d5f829"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032365153
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 136, 'threshold': 50, 'total_amount': 53909720, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 135, 'first_seen': 1760285764, 'matching_hash': 'db9686895aceb522'}}}