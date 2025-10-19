```json
{
  "id": "4ab2bf463c44a3e1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292663,
  "host_pid": "9e6742732c60:1",
  "hash": "20905a53213846ffd714c2db409e8cf59fff4a143a48db7fb15154759081b989",
  "cid": "QmV120905a53213846ffd714c2db409e8cf59fff4a14",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292663,
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
      "evaluated_at": 1760292663
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
  "sig": "8547400dac62f46438332d2569e65e00ea99ef8cc6a97341a77a5e1a831f18a6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025001245
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 202, 'threshold': 50, 'total_amount': 43137706, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 201, 'first_seen': 1760285764, 'matching_hash': 'bf601f225a65579b'}}}