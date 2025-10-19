```json
{
  "id": "618ab4b7b9a7fa87",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292653,
  "host_pid": "9e6742732c60:1",
  "hash": "29b19d8e340cc77ce2a7739d258d95994dce7d8cffe5eb6b0d957ffa7d891706",
  "cid": "QmV129b19d8e340cc77ce2a7739d258d95994dce7d8c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292653,
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
      "evaluated_at": 1760292653
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
  "sig": "0b42886237228515ea0561818454cc2c7bee185b7e24938919c62914bffedf7b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462094881
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 202, 'threshold': 50, 'total_amount': 96315620, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 201, 'first_seen': 1760285763, 'matching_hash': '1dac8a668721a731'}}}