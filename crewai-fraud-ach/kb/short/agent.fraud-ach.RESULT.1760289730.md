```json
{
  "id": "5b53d5e46b5b5d14",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289730,
  "host_pid": "9e6742732c60:1",
  "hash": "7e019fa916b059eae4bf55a1c9e4d0cc57cbdb27e460790355671636c40a5e6f",
  "cid": "QmV17e019fa916b059eae4bf55a1c9e4d0cc57cbdb27",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289730,
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
      "evaluated_at": 1760289730
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
  "sig": "021831f4167547473807816c2537b15c0b2a9915a51896faf8f89dee0e6bdf13"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100273377315
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 131, 'threshold': 50, 'total_amount': 28398704, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 130, 'first_seen': 1760285765, 'matching_hash': '3946d3a9787ed734'}}}