```json
{
  "id": "55c84a929dd36794",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287908,
  "host_pid": "9e6742732c60:1",
  "hash": "0d6a89d69c4091ced9bd9910790f8e85c25c7f821dd20d22ea29987cc95bf4ff",
  "cid": "QmV10d6a89d69c4091ced9bd9910790f8e85c25c7f82",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287908,
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
      "evaluated_at": 1760287908
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
  "sig": "0fdbe37a926b4fc6e4d5fd116d91d6ea5bc892068044c861945a0beebac49674"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105159904059
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 76, 'threshold': 50, 'total_amount': 34115488, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 75, 'first_seen': 1760285764, 'matching_hash': '7ad1725ffd2dadfd'}}}