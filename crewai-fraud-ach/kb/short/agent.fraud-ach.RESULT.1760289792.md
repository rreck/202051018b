```json
{
  "id": "1922045197af3c3f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289792,
  "host_pid": "9e6742732c60:1",
  "hash": "f6dd1d6883aa1a0247697edfcaf5ffa039b1d8992edf3e4a14fba79ebb4d365d",
  "cid": "QmV1f6dd1d6883aa1a0247697edfcaf5ffa039b1d899",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289792,
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
      "evaluated_at": 1760289792
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
  "sig": "16e69b985519d235510e5885921a97d29792053928c235d1747dc84088249c97"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009594081907
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 133, 'threshold': 50, 'total_amount': 65908682, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 132, 'first_seen': 1760285763, 'matching_hash': 'b8f6a044d6b1da81'}}}