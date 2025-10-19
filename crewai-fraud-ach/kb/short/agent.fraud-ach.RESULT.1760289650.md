```json
{
  "id": "7196645c101ba48d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289650,
  "host_pid": "9e6742732c60:1",
  "hash": "a1eb985c704dc8c90dfaabe52861e0ba2d23bb6ee89cb230b21ff1d18153ad37",
  "cid": "QmV1a1eb985c704dc8c90dfaabe52861e0ba2d23bb6e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289650,
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
      "evaluated_at": 1760289650
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
  "sig": "1491b1445e853ebd6ca9d884808e4c41eff756685491e3e42511d6874d96d79c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026697062
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 205, 'threshold': 50, 'total_amount': 65451990, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 204, 'first_seen': 1760284979, 'matching_hash': 'f9d80f2e7cffa5ec'}}}