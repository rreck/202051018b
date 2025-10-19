```json
{
  "id": "3d4c01c10eca7194",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289204,
  "host_pid": "9e6742732c60:1",
  "hash": "869033acc36b1c7cad07d707d702de792d30c2545eec84a3f88c35e85ebddfcf",
  "cid": "QmV1869033acc36b1c7cad07d707d702de792d30c254",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289204,
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
      "evaluated_at": 1760289204
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
  "sig": "4c795ec14a9967be9230dc6f5e5df27ac580d6056588d5e1173e2047b47f149a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023496704
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 116, 'threshold': 50, 'total_amount': 39330148, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 115, 'first_seen': 1760285765, 'matching_hash': 'f379baac52e28232'}}}