```json
{
  "id": "670c8d0e31a179ab",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287904,
  "host_pid": "9e6742732c60:1",
  "hash": "bc4aad8f3e51cc60e9ccf4bdef1164edab48154a59393efb81cb652ad63128c3",
  "cid": "QmV1bc4aad8f3e51cc60e9ccf4bdef1164edab48154a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287904,
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
      "evaluated_at": 1760287904
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
  "sig": "c7263567a64d366227b052ae04912e009543792946ae58e4e8cb9c477519df0f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026132147
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 76, 'threshold': 50, 'total_amount': 13785868, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 75, 'first_seen': 1760285765, 'matching_hash': 'fe0c58008e192989'}}}