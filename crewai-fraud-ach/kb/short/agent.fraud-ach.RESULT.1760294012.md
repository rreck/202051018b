```json
{
  "id": "ac95bce6e7fcab75",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294012,
  "host_pid": "9e6742732c60:1",
  "hash": "f0b49c84d6a4ccbe03f6e8283e18c69891b8fbf3c54939d3f015a2a2b5811eb8",
  "cid": "QmV1f0b49c84d6a4ccbe03f6e8283e18c69891b8fbf3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294012,
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
      "evaluated_at": 1760294012
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
  "sig": "2f3a773f15188414e517e56e1566267a654497b98d4dea0538c87be53c7b157e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000247065619
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 230, 'threshold': 50, 'total_amount': 91969410, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 229, 'first_seen': 1760285763, 'matching_hash': '73a93f9011d99735'}}}