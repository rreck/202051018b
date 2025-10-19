```json
{
  "id": "beac09d3049076aa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293052,
  "host_pid": "9e6742732c60:1",
  "hash": "cc375e31a8b067c8edf4b15a18ba6ba22b5e50a19217de56e69d0e05c754f583",
  "cid": "QmV1cc375e31a8b067c8edf4b15a18ba6ba22b5e50a1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293052,
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
      "evaluated_at": 1760293052
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
  "sig": "51aa4bdb5604ac7960dd55d04ed49830be97ade56f003b86b129bdf596be0ac9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105151363741
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 210, 'threshold': 50, 'total_amount': 91017990, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 209, 'first_seen': 1760285765, 'matching_hash': 'ec824383c23ded7d'}}}