```json
{
  "id": "74d161874465fcc6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289822,
  "host_pid": "9e6742732c60:1",
  "hash": "b1683b4f8059ec0db87d35fea14a7c08adc542e1848405eb10a3c71743220fbf",
  "cid": "QmV1b1683b4f8059ec0db87d35fea14a7c08adc542e1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289822,
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
      "evaluated_at": 1760289822
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
  "sig": "df357effe529396568340a5a029275e50307c14474f8f8145ec6ea22637dbc28"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000247026993
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 134, 'threshold': 50, 'total_amount': 58991222, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 133, 'first_seen': 1760285764, 'matching_hash': '7c7d13001f766fd7'}}}