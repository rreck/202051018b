```json
{
  "id": "fb2bf0d0f8441f8f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291037,
  "host_pid": "9e6742732c60:1",
  "hash": "51ee389b8ff318d2c2a4f08df18b0782afe859cbc4377950d62069ce441b9f7d",
  "cid": "QmV151ee389b8ff318d2c2a4f08df18b0782afe859cb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291037,
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
      "evaluated_at": 1760291037
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
  "sig": "04e88ac8fc734da106f42ffc2666c054738c7d0ff477354831995ddec5cb647f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027147487
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 165, 'threshold': 50, 'total_amount': 82467660, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 164, 'first_seen': 1760285765, 'matching_hash': 'f2056111b893f4fa'}}}