```json
{
  "id": "5eb95514a7950828",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294041,
  "host_pid": "9e6742732c60:1",
  "hash": "8ab576bb66ae9be0aa713a989a7e7a555c97504486064507fdc04a5e7c720cd1",
  "cid": "QmV18ab576bb66ae9be0aa713a989a7e7a555c975044",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294041,
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
      "evaluated_at": 1760294041
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
  "sig": "cacbbe73d55eee38fa7c2fe4f00fe47c1784523e972b5c3646ce32fac8ad0aa4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000020807792
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 230, 'threshold': 50, 'total_amount': 48012730, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 229, 'first_seen': 1760285764, 'matching_hash': '8390351bce6e669b'}}}