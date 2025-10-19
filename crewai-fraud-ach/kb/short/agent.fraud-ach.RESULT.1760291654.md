```json
{
  "id": "b73fff81c3c39bc2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291654,
  "host_pid": "9e6742732c60:1",
  "hash": "1dfc5b315e2f53ab7aac15cf098c48fd9b80a74118c59efb3b95eb9c11a59748",
  "cid": "QmV11dfc5b315e2f53ab7aac15cf098c48fd9b80a741",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291654,
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
      "evaluated_at": 1760291655
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
  "sig": "20b65d2275719f5a838f4204b14e653d34eb3f32e927c287adfff6c56f2535e2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596354415
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 180, 'threshold': 50, 'total_amount': 50100300, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 179, 'first_seen': 1760285763, 'matching_hash': 'f20df65cb297838c'}}}