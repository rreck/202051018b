```json
{
  "id": "b17527287ce664db",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294593,
  "host_pid": "9e6742732c60:1",
  "hash": "2d99b17e8f324d72ed026ba8b460a4c698224607d185d58255a3c94d957f3ff6",
  "cid": "QmV12d99b17e8f324d72ed026ba8b460a4c698224607",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294593,
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
      "evaluated_at": 1760294593
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
  "sig": "ccabaaa9e5c28da93aff6d3bc74a6ece78ea593bcff6cfc0a9fbf15a3647944e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031959136
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 241, 'threshold': 50, 'total_amount': 18560133, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 240, 'first_seen': 1760285763, 'matching_hash': 'f67377943b0624b0'}}}