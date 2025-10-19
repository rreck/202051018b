```json
{
  "id": "af600163b5db489f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290536,
  "host_pid": "9e6742732c60:1",
  "hash": "7cad390a5895076e93d60800287455f31537fc134528564697e2d31a91a4c121",
  "cid": "QmV17cad390a5895076e93d60800287455f31537fc13",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290536,
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
      "evaluated_at": 1760290536
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
  "sig": "5bc141f0c5a666d6202303d741afebdd2fc93a08fe634045dd65c8cd1c7de907"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025654087
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 153, 'threshold': 50, 'total_amount': 21388635, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 152, 'first_seen': 1760285763, 'matching_hash': '431eabbdd05dc2b1'}}}