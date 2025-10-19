```json
{
  "id": "d1a25c53bb217dfb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290135,
  "host_pid": "9e6742732c60:1",
  "hash": "9a60a52bef5694fc19b92c1d76fd11088cfaf9507e3647e04fc24222d1516b82",
  "cid": "QmV19a60a52bef5694fc19b92c1d76fd11088cfaf950",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290135,
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
      "evaluated_at": 1760290135
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
  "sig": "561b28c536529bcc4ef21e2c1be94fccc6aa841193c0ba108aa7ebd68cbdba40"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026887900
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 142, 'threshold': 50, 'total_amount': 45499498, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 141, 'first_seen': 1760285765, 'matching_hash': '21e48734f91c19c6'}}}