```json
{
  "id": "4028071f7354f8e2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288804,
  "host_pid": "9e6742732c60:1",
  "hash": "20d4a11d5083ee0520c304ac78f8e14fe5546b10a5856fdeec555b24089638c1",
  "cid": "QmV120d4a11d5083ee0520c304ac78f8e14fe5546b10",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288804,
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
      "evaluated_at": 1760288804
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
  "sig": "bd99830b829a5fcc3a18dc5c3f64cfab85306f3554fc0e3f5eb8d21dbba4b1ae"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 104, 'threshold': 50, 'total_amount': 33097792, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 103, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}