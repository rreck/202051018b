```json
{
  "id": "6042869c7780106f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289250,
  "host_pid": "9e6742732c60:1",
  "hash": "4357ed6552c83d587ad6f86fea6ff87a7bdec13af9f22fd82f273b6073dce482",
  "cid": "QmV14357ed6552c83d587ad6f86fea6ff87a7bdec13a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289250,
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
      "evaluated_at": 1760289250
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
  "sig": "da8eaef390383605fefb2c1b08ab557d75d8d150a2df8cc8b83028abcdda0dde"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591278492
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 118, 'threshold': 50, 'total_amount': 14717668, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 117, 'first_seen': 1760285763, 'matching_hash': '3e8e4f28808ab222'}}}