```json
{
  "id": "a4f5c67e2c3eae08",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290380,
  "host_pid": "9e6742732c60:1",
  "hash": "36d32ee5421e8b3004673462ec57ec4434612dd0cef1b05740fbd24b2b5590d0",
  "cid": "QmV136d32ee5421e8b3004673462ec57ec4434612dd0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290380,
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
      "evaluated_at": 1760290380
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
  "sig": "6b50f1ee87614f5727c06b9fcf1a4d3a088ee0811a412610fc067c61d038bb08"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156708491
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 149, 'threshold': 50, 'total_amount': 14480714, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 148, 'first_seen': 1760285763, 'matching_hash': '1bac7a606fc9693a'}}}