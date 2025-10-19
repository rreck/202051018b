```json
{
  "id": "3431ce69ebb22193",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288005,
  "host_pid": "9e6742732c60:1",
  "hash": "a246b9416000a72050f33b68ca91642cebf88666bef4d5d54529fbaf9057c36e",
  "cid": "QmV1a246b9416000a72050f33b68ca91642cebf88666",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288005,
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
      "evaluated_at": 1760288005
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
  "sig": "352352810bfd44463e269493f6a470d0cd433d5d101edd4f859b43659524be69"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 79, 'threshold': 50, 'total_amount': 25141592, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 78, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}