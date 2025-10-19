```json
{
  "id": "0843df5d7de12bac",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294818,
  "host_pid": "9e6742732c60:1",
  "hash": "8bee8ad6fe997f1f595e79ab4a4127eef0c4c3f335e054e7859853f89f8f8bd3",
  "cid": "QmV18bee8ad6fe997f1f595e79ab4a4127eef0c4c3f3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294818,
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
      "evaluated_at": 1760294818
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
  "sig": "6ea115dd34e3c86569fc721e126096e485f68225b22205dcf9f9b1761096692a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100276179264
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 245, 'threshold': 50, 'total_amount': 42006720, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 244, 'first_seen': 1760285763, 'matching_hash': 'cb2614db0e970d70'}}}}