```json
{
  "id": "ae7038a9ae846fe1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292424,
  "host_pid": "9e6742732c60:1",
  "hash": "bfe7fb56703efc4b313947cad9c9a26fe5aa6696ed537004e8a20397d5e52f52",
  "cid": "QmV1bfe7fb56703efc4b313947cad9c9a26fe5aa6696",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292424,
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
      "evaluated_at": 1760292424
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_high"
  ],
  "sig": "6d5e791bc8a5034549b7834c6bd8cd439f6555b7b685bbb7634dd3c3c644d750"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 021000028490637
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 197, 'threshold': 50, 'total_amount': 98500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 196, 'first_seen': 1760285765, 'matching_hash': '1f028817acc0361c'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}