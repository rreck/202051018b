```json
{
  "id": "1a56df2083be219e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293781,
  "host_pid": "9e6742732c60:1",
  "hash": "7611d913e853536c28c14a9d042f4519311141aef94e55b4a4c5b129b1988d40",
  "cid": "QmV17611d913e853536c28c14a9d042f4519311141ae",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293781,
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
      "evaluated_at": 1760293781
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
  "sig": "8ab7a49901f861490c4a840830f40d8515e9a143aba76afce705e4521e11df9c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460501611
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 225, 'threshold': 50, 'total_amount': 38162475, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 224, 'first_seen': 1760285764, 'matching_hash': 'a26573d157351ea4'}}}