```json
{
  "id": "f3d6d09ea005bf26",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288296,
  "host_pid": "9e6742732c60:1",
  "hash": "9388491408fa8438796e8193b56a5c594e611a24c61ad64ff443967c70c849a2",
  "cid": "QmV19388491408fa8438796e8193b56a5c594e611a24",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288296,
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
      "evaluated_at": 1760288296
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
  "sig": "000d6ef15ef5092796c6906db79be9fbe2bcab3d4340a64b62ed098b0192db17"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242331672
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 89, 'threshold': 50, 'total_amount': 10297834, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 88, 'first_seen': 1760285763, 'matching_hash': '532e279550beef55'}}}