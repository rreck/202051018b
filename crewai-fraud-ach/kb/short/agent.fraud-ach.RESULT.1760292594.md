```json
{
  "id": "42ee46c68e3330b4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292594,
  "host_pid": "9e6742732c60:1",
  "hash": "0dc9c2f215cca558cef2465fe62394644fa89006cdb6bd6615c7342f8a183fac",
  "cid": "QmV10dc9c2f215cca558cef2465fe62394644fa89006",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292594,
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
      "evaluated_at": 1760292594
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
  "sig": "eff31b0115b14a39cb595f5073e90e131bcf52635e49f81d96630d699ef3702f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037838000
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 201, 'threshold': 50, 'total_amount': 23494689, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 200, 'first_seen': 1760285763, 'matching_hash': 'ae4ad01d54e54763'}}}nd_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}