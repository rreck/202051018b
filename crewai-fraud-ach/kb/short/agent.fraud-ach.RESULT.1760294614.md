```json
{
  "id": "ec4e4619819d4a7c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294614,
  "host_pid": "9e6742732c60:1",
  "hash": "27ed44c1faca843416804c01356e3f30e4873c4d0c2c246d3bf4d85755df3df8",
  "cid": "QmV127ed44c1faca843416804c01356e3f30e4873c4d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294614,
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
      "evaluated_at": 1760294614
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
  "sig": "0e9a9c50968f1c2aa9330f99ce65f188e9e30da21aa72cb742b9427aae769387"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000249454336
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 241, 'threshold': 50, 'total_amount': 35790669, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 240, 'first_seen': 1760285763, 'matching_hash': '6b4cd9d1923f5d4e'}}}