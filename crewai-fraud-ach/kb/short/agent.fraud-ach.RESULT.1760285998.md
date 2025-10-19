```json
{
  "id": "83d1272540b73aa2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285998,
  "host_pid": "9e6742732c60:1",
  "hash": "03c2ff88d8bab84d95f4d02aa5515d72ee191e1abff6e523cfbc071b74882de3",
  "cid": "QmV103c2ff88d8bab84d95f4d02aa5515d72ee191e1a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285998,
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
      "evaluated_at": 1760285998
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
  "sig": "551c5a348766fbffa8bd22cec5e012f3a099f623e376e1c6021f57577d0b3b72"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201460204606
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 10, 'first_seen': 1760285763, 'matching_hash': 'ff63dbf095b2d177'}}}