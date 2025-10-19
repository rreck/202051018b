```json
{
  "id": "76b52c439f3441ee",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291677,
  "host_pid": "9e6742732c60:1",
  "hash": "d8f17817568547868abddc1b3bbd839b7a98dbb39262bd1396678483e7e3ae80",
  "cid": "QmV1d8f17817568547868abddc1b3bbd839b7a98dbb3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291677,
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
      "evaluated_at": 1760291677
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
  "sig": "958b5f6b5bdb97e4d92999240f5972da4aa585f65cc73f81ab1749d175b49cb3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 180, 'threshold': 50, 'total_amount': 57284640, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 179, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}