```json
{
  "id": "8d161555f837f179",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291739,
  "host_pid": "9e6742732c60:1",
  "hash": "2a3017b7943a1c4b931801d01e88ce3285d17c4184aabe020269ced4c44cd988",
  "cid": "QmV12a3017b7943a1c4b931801d01e88ce3285d17c41",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291739,
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
      "evaluated_at": 1760291739
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
  "sig": "b397446cf0890beca4043adb031664e56175e45eee8bce20876bf0a1f701bf0a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024762963
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 182, 'threshold': 50, 'total_amount': 18200000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 181, 'first_seen': 1760285764, 'matching_hash': 'dd3a0eba0797b423'}}}