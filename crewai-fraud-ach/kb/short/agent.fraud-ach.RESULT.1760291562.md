```json
{
  "id": "b4661221f202ec23",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291562,
  "host_pid": "9e6742732c60:1",
  "hash": "3414b4f55cae7a031efbf0e2ab1652a140c6d468c22341c09aabd92f196da39f",
  "cid": "QmV13414b4f55cae7a031efbf0e2ab1652a140c6d468",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291562,
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
      "evaluated_at": 1760291562
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
  "sig": "4debaebb288e457cece7ae6d6bed1db11439fc613f92fc4c00cf33b985a9507a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000020127754
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 178, 'threshold': 50, 'total_amount': 33485716, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 177, 'first_seen': 1760285763, 'matching_hash': '0e6816faa7d68d85'}}}