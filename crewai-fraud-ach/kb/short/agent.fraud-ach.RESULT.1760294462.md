```json
{
  "id": "8ded6944ca82c989",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294462,
  "host_pid": "9e6742732c60:1",
  "hash": "73d5c334d3af348ff4ada73b0a9aa90359d2753fc7f578f8b5c03b91210f7bae",
  "cid": "QmV173d5c334d3af348ff4ada73b0a9aa90359d2753f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294462,
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
      "evaluated_at": 1760294462
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
  "sig": "330fb30efec597e4a029ad32372823b4c39f8efb04dd13ba40f486e9ed2fa399"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105159904059
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 238, 'threshold': 50, 'total_amount': 106835344, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 237, 'first_seen': 1760285764, 'matching_hash': '7ad1725ffd2dadfd'}}}