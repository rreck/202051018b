```json
{
  "id": "c59b7f66d1cb0909",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293905,
  "host_pid": "9e6742732c60:1",
  "hash": "491f3f89b5461a1ebc0c3c7ee1feb8f7a0299218764bad450414e093f8f63e61",
  "cid": "QmV1491f3f89b5461a1ebc0c3c7ee1feb8f7a0299218",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293905,
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
      "evaluated_at": 1760293905
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
  "sig": "3cf51deae5665e8bbd642baea83884511d19c1859ecf193a89940cd9143ca849"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274159227
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 228, 'threshold': 50, 'total_amount': 28596672, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 227, 'first_seen': 1760285763, 'matching_hash': 'c6403d45da933f2b'}}}