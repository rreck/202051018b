```json
{
  "id": "fe635bee5c0fdaa7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293501,
  "host_pid": "9e6742732c60:1",
  "hash": "c677b51d4476c051f1b302b9827af5601143c86092118173181d79689ceef6b9",
  "cid": "QmV1c677b51d4476c051f1b302b9827af5601143c860",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293501,
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
      "evaluated_at": 1760293501
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
  "sig": "65e6177bccec86a5f15eadd20835b9279209ab2670b28787b445aa038235e6e3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460208894
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 220, 'threshold': 50, 'total_amount': 105783700, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 219, 'first_seen': 1760285763, 'matching_hash': '36d88bd4e0ec214b'}}}