```json
{
  "id": "c813764fabd05de0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292890,
  "host_pid": "9e6742732c60:1",
  "hash": "113ee625ff005adee29189aa85f3d7f27e8558f94fd0a07bed83277fd19e7034",
  "cid": "QmV1113ee625ff005adee29189aa85f3d7f27e8558f9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292890,
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
      "evaluated_at": 1760292890
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
  "sig": "da55341fd014024b157271a13d4a97e010c1ac8e9850aad39c5b69acc6d8fab5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027976584
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 207, 'threshold': 50, 'total_amount': 63876681, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 206, 'first_seen': 1760285763, 'matching_hash': '76d4e63915320a3d'}}}