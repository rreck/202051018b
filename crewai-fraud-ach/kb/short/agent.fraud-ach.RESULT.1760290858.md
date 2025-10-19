```json
{
  "id": "e0aabf035c68cf95",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290858,
  "host_pid": "9e6742732c60:1",
  "hash": "b75ae2ee448db338412f4bda43a014ec5058f0eecd5090c959aadc49d17ee89a",
  "cid": "QmV1b75ae2ee448db338412f4bda43a014ec5058f0ee",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290858,
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
      "evaluated_at": 1760290858
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
  "sig": "3615986c8d0695952932173fe1466937ed710a2810fc73b4d6d5d191657bf536"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021861158
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 161, 'threshold': 50, 'total_amount': 41251098, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 160, 'first_seen': 1760285763, 'matching_hash': '4f96dd6d0eca8862'}}}