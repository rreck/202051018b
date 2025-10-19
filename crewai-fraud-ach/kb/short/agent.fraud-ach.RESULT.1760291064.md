```json
{
  "id": "3a144b7ab8cdd0ba",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291064,
  "host_pid": "9e6742732c60:1",
  "hash": "04b0061539c68717c7e960f28b8a0cda75397b1c763ecb567816aa8e85da39dc",
  "cid": "QmV104b0061539c68717c7e960f28b8a0cda75397b1c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291064,
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
      "evaluated_at": 1760291064
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
  "sig": "e067597ffe639ac6dcac93ea4abcd698f9efd5eb2d4171333686772943117bb7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598774484
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 166, 'threshold': 50, 'total_amount': 32726402, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 165, 'first_seen': 1760285764, 'matching_hash': 'dadabb4a69349ebb'}}}