```json
{
  "id": "f42f71751c2f976d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288507,
  "host_pid": "9e6742732c60:1",
  "hash": "060f003479c8dfb128e7cd06fb8f13f64baaf07373cfdd0701e8f3a38b5c35bb",
  "cid": "QmV1060f003479c8dfb128e7cd06fb8f13f64baaf073",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288507,
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
      "evaluated_at": 1760288507
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
  "sig": "ac6f9c44e20ce5a51020e3976af52e58516398224b6fa3615da85a388fedeb5b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000021513577
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 95, 'threshold': 50, 'total_amount': 21657625, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 94, 'first_seen': 1760285765, 'matching_hash': '2d9e7d16ad0b5ba4'}}}