```json
{
  "id": "1d473acefa434665",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291710,
  "host_pid": "9e6742732c60:1",
  "hash": "20b45c441dc87d04d3f3cb591e40229659281b7d60bf48d5be296de8cec22c92",
  "cid": "QmV120b45c441dc87d04d3f3cb591e40229659281b7d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291710,
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
      "evaluated_at": 1760291710
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
  "sig": "34ea50dffa42422a7d7854ba8a1b229d7c391bcc0ef263df343d4e761ff9508d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027064013
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 181, 'threshold': 50, 'total_amount': 53871754, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 180, 'first_seen': 1760285765, 'matching_hash': '811cb7a859f68158'}}}