```json
{
  "id": "c0a347b80d8f22eb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289166,
  "host_pid": "9e6742732c60:1",
  "hash": "2b5fd9ba8883ed08bbb0391f4976814c0d677ef0117420e0738a7e31e19e1e83",
  "cid": "QmV12b5fd9ba8883ed08bbb0391f4976814c0d677ef0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289166,
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
      "evaluated_at": 1760289166
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
  "sig": "74e16353c3db022eaf702073cdeff057b30180d3632d0b5d708e6e67fdaac42f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596862432
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 115, 'threshold': 50, 'total_amount': 23466440, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 114, 'first_seen': 1760285764, 'matching_hash': 'ec6d2f2d96a1a77c'}}}