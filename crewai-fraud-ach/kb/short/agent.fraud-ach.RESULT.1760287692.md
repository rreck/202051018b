```json
{
  "id": "b9020eeb7253f0cb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287692,
  "host_pid": "9e6742732c60:1",
  "hash": "30e30c37a27e8c793a314fdc8d8d9869094ef441d381873b6a339348266a8ba3",
  "cid": "QmV130e30c37a27e8c793a314fdc8d8d9869094ef441",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287692,
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
      "evaluated_at": 1760287692
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
  "sig": "c5be7684c8d254cc5bcbd0494085edb165e3e622a6e15a52dca9aee51f66dc4e"
}
```

Fraud detected: duplicate_transaction (score: 86)
Transaction: 111000022462179
Details: {'velocity': {'fraud_detected': True, 'risk_score': 88, 'details': {'transaction_count': 69, 'threshold': 50, 'total_amount': 28001925, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 68, 'first_seen': 1760285763, 'matching_hash': 'b017d6ab8abfffc0'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}