```json
{
  "id": "c4a786ca97fd20b6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289718,
  "host_pid": "9e6742732c60:1",
  "hash": "b981622821c212fc34c7312c61e64ed2b9ee2f811c06e153181318bfeb01be40",
  "cid": "QmV1b981622821c212fc34c7312c61e64ed2b9ee2f81",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289718,
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
      "evaluated_at": 1760289718
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
  "sig": "f460bf7333a7ba43ad4b14ad9a1a0be673859ed6924b7a08a8159053e0a05a08"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026302865
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 131, 'threshold': 50, 'total_amount': 39373884, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 130, 'first_seen': 1760285763, 'matching_hash': '15ebb46c9afca80b'}}}