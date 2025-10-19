```json
{
  "id": "b321958be17cf5f0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292638,
  "host_pid": "9e6742732c60:1",
  "hash": "2419b9ff308184b86a6fe3994bf468619559adbfad350f5937a4f243b5834109",
  "cid": "QmV12419b9ff308184b86a6fe3994bf468619559adbf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292638,
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
      "evaluated_at": 1760292638
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
  "sig": "6935058ee319bbf3181aef17167121b76e7001445b7314f594742900b811e1e9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201466107420
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 202, 'threshold': 50, 'total_amount': 81794648, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 201, 'first_seen': 1760285763, 'matching_hash': 'b2544ae352aa282b'}}}